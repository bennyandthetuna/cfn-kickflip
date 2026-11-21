#ruff: noqa: E501
"""
Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

---
cfn-kickflip
Copyright 2026 Ben Lampert
This product is a modified fork of AWS CloudFormation Template Flip
(https://github.com/awslabs/aws-cfn-template-flip), updates for modern
Python runtimes and packaging

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License. 
A copy of the License is located at

    https://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. 
This file is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions 
and limitations under the License.
"""
import inspect
import logging
import os
from typing import Any, NamedTuple

_logger: logging.Logger = logging.getLogger(__name__)


class _ConfigArg(NamedTuple):
    dtype: type
    nullable: bool = True
    has_default: bool = False
    default: Any = None


_CONFIG_DEFAULTS: dict[str, _ConfigArg] = {
    "max_col_width": _ConfigArg(dtype=int, 
                                nullable=False, 
                                has_default=True, 
                                default=200
                                )}


class _Config:
    """Cfn_flip's Configuration class."""

    # __slots__ = (f"_{attr}" for attr in _CONFIG_DEFAULTS)

    def __init__(self):
        for name, conf in _CONFIG_DEFAULTS.items():
            self._load_config(name=name, conf=conf)

    def _load_config(self, name, conf):
        env_var_name: str = f"CFN_{name.upper()}"
        env_var: str | None = os.getenv(env_var_name)
        if env_var is not None:
            value = self._apply_type(
                name=name, 
                value=env_var, 
                dtype=_CONFIG_DEFAULTS[name].dtype, 
                nullable=_CONFIG_DEFAULTS[name].nullable
            )
            self.__setattr__(name, value)
        elif conf.has_default is True:
            self.__setattr__(name, conf.default)

    def __getattr__(self, item: str) -> Any:
        if item in _CONFIG_DEFAULTS:
            return super().__getattribute__(f"_{item}")
        raise AttributeError

    def __getitem__(self, item: str) -> Any:
        return self.__getattr__(item)

    def __setattr__(self, key: str, value: Any) -> Any:
        if key not in _CONFIG_DEFAULTS:
            raise TypeError(
                f"{key} is not a valid configuration. " f"Please use: {list(_CONFIG_DEFAULTS.keys())}"
            )
        value = self._apply_type(
            name=key, 
            value=value, 
            dtype=_CONFIG_DEFAULTS[key].dtype, 
            nullable=_CONFIG_DEFAULTS[key].nullable
        )
        super().__setattr__(f"_{key}", value)

    def reset(self, item: str | None = None) -> None:
        """Reset one or all (if None is received) configuration values.

        Parameters
        ----------
        item : str, optional
            Configuration item name.

        Returns
        -------
        None
            None.

        Examples
        --------
        >>> import cfn_flip
        >>> cfn_flip.config.reset("max_col_width")  # Reset one specific configuration
        >>> cfn_flip.config.reset()  # Reset all

        """
        if item is None:
            for name, conf in _CONFIG_DEFAULTS.items():
                delattr(self, f"_{name}")
                self._load_config(name=name, conf=conf)
        else:
            delattr(self, f"_{item}")
            self._load_config(name=item, conf=_CONFIG_DEFAULTS[item])

    @staticmethod
    def _apply_type(name: str, value: Any, dtype: type, nullable: bool) -> Any:
        if _Config._is_null(value=value) is True:
            if nullable is True:
                return None
            ValueError(
                f"{name} configuration does not accept null value." f" Please pass {dtype}."
            )
        if isinstance(value, dtype) is False:
            value = dtype(value)
        return value

    @staticmethod
    def _is_null(value: Any) -> bool:
        if value is None:
            return True
        if (isinstance(value, str) is True) and (value.lower() in ("none", "null", "nil")):
            return True
        return False


def apply_configs(function):
    """Decorate some function with configs."""
    signature = inspect.signature(function)
    args_names = list(signature.parameters.keys())
    valid_configs = [x for x in _CONFIG_DEFAULTS if x in args_names]

    def wrapper(*args, **kwargs):
        received_args = signature.bind_partial(*args, **kwargs).arguments
        available_configs = [x for x in valid_configs if (x not in received_args) and (hasattr(config, x) is True)]
        missing_args = {x: config[x] for x in available_configs}
        final_args = {**received_args, **missing_args}
        return function(**final_args)

    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__
    wrapper.__signature__ = signature
    return wrapper


config: _Config = _Config()
