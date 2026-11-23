# Security Policy

## Supported Versions

We only support `2.x` release line with security updates. We do not provide patches for the `1.x` series, which belongs to the archived upstream project `awslabs/aws-template-flip` repository. 

| Version | Supported          | Notes |
| ------- | ------------------ |-------|
|>=2.0.0.x| :white_check_mark: | Active `cfn-kickflip` releases.|
| < 2.0.0 | :x:                | Legacy `aws-cfn-template-flip` releases (archived upstream).|

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public Github issues.**

Instead, please report them using [Github's Private Vulnerability Reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability) feature on this repository.

If private vulnerability reporting is not enabled, or you prefer email, please contact the maintainer directly at **[ben.lampert@protonmail.com]**

### What to include in your report
To help us resolve the issue quickly , please provide:
* A description of the vulnerability and its potential impact.
* Steps to reproduce the issue (a proof-of-concept Cloudformation template or script is highly appreciated).
* The version of `cfn-kickflip` affected.
* Your operating system and Python version.

## Response Process
1. **Acknowledgement:** You will receive a response acknowledging receipt of your report within 48 hours.
2. **Triage:** The maintainer will verify the vulnerability and determine its severity.
3. **Patching:** A fix will be developed and tested privately.
4. **Release:** A new patch version will be published to PyPI, and a Github Security Advisory (CVE/GHSA) will be published to inform the community. You will be credited for the discovery in the advisory unless you request to remain anonymous.
