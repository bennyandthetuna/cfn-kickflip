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

from cfn_tools.yaml_dumper import CfnYamlDumper


class CleanCfnYamlDumper(CfnYamlDumper):
    """
    Format multi-line strings with |
    """

    def represent_scalar(self, tag, value, style=None):
        if "\n" in value:
            style = "|"

        return super().represent_scalar(tag, value, style)
