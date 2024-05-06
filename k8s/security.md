# Links Pages
- [ksoc-labs awesome-k8s-security](https://github.com/ksoclabs/awesome-kubernetes-security)

# Starting Points
- [Securing Kubernetes: A Comprehensive Guide to Runtime Security and System Hardening](https://medium.com/@seifeddinerajhi/securing-kubernetes-a-comprehensive-guide-to-runtime-security-and-system-hardening-33f5a5328f1)
- [OWASP K8S Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)  and [OWAS K8S Top Ten](https://github.com/OWASP/www-project-kubernetes-top-ten/tree/main)
- [Vinum Security K8S Checklist](https://github.com/Vinum-Security/kubernetes-security-checklist)
- [Official Kubernetes Checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
- [Risk Analysis of K8S Clusters](https://tldrsec.com/p/guides-kubernetes) - Jun 2023
- [Kubernetes Security Best Practices](https://github.com/freach/kubernetes-security-best-practice)

# Knobs
- [Kubernetes API Server Bypass Risks](https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/)

## Pod
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

# TTPs / ATT&CK
- [Mitre ATT&CK Matrix for Kubernetes](https://www.magalix.com/blog/mitre-attck-matrix-for-kubernetes)
- [Mitre Container ATT&CK](https://attack.mitre.org/matrices/enterprise/containers/)
- [Mapping Risks and Threats in Kubernetes to the MITRE ATT&CK Framework](https://blog.aquasec.com/mitre-attack-framework-for-containers)
- [Center for Threat-Informed Defense teams up with Microsoft, partners to build the ATT&CK® for Containers matrix](https://www.microsoft.com/security/blog/2021/04/29/center-for-threat-informed-defense-teams-up-with-microsoft-partners-to-build-the-attck-for-containers-matrix/)
- [The Current State of K8S Threat Modeling](https://blog.marcolancini.it/2020/blog-kubernetes-threat-modelling/)
- [CNCF k8s-threat-model](https://github.com/cncf/financial-user-group/tree/main/projects/k8s-threat-model)
- [NCC K8S Threat Model](https://research.nccgroup.com/2017/11/23/kubernetes-security-consider-your-threat-model/)
- [CloudSecDocs K8S Threat Model](https://cloudsecdocs.com/container_security/theory/threats/k8s_threat_model/)

# Attacking & Defending
- [KubeCon NA 2019 CTF Guide](https://github.com/securekubernetes/securekubernetes/)
- [Attacking and Defending K8S Cluster](https://www.youtube.com/watch?v=UdMFTdeAL1s) - Tutorial: Attacking and Defending Kube... Brad Geesaman, Jimmy Mesta, Tabitha Sable & Peter Benjamin (November 2019) 
- [OWASP K8S Top Ten](https://github.com/OWASP/www-project-kubernetes-top-ten)
- [CKSS Materials](https://github.com/walidshaari/Certified-Kubernetes-Security-Specialist)

# Azure
- [Microsoft Defender for Containers](https://docs.microsoft.com/en-us/azure/defender-for-cloud/defender-for-containers-introduction)
- [Security alerts - a reference guide](https://docs.microsoft.com/en-us/azure/defender-for-cloud/alerts-reference#alerts-k8scluster)

# EKS & Guard Duty
- [Guide to AWS GuardDuty findings in EKS](https://medium.com/@cloud_tips/guide-to-aws-guardduty-findings-in-eks-62babbd7da88)
- [EKS Best Practices for Security](https://aws.github.io/aws-eks-best-practices/security/docs/)
- [hardeneks](https://github.com/aws-samples/hardeneks) - Runs checks to see if an EKS cluster follows EKS Best Practices.


# GKE
- [GKE Harden Your Cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)

# Admission Controllers
- [What is an AC](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) - from K8S docs
- [kyverno](https://kyverno.io/)

# Namespace Boundaries 
- [NamespaceHound: protecting multi-tenant K8s clusters](https://www.wiz.io/blog/introducing-namespacehound-for-cross-tenant-violation-assessments)


# Comparisons
- [Threat Detection on EKS – Comparing Falco and GuardDuty For EKS Protection](https://dev.to/aws-builders/threat-detection-on-eks-comparing-falco-and-guardduty-for-eks-protection-2m6b) 
- [EKS Best Practice Guide - Security](https://aws.github.io/aws-eks-best-practices/security/docs/)

# Logging and SIEM
- [Monitoring Kubernetes sensitive object access](https://lantern.splunk.com/Security/Use_Cases/Threat_Hunting/Monitoring_Kubernetes_sensitive_object_access)
- [Threat Hunting with Kubernetes Audit Logs](https://developer.squareup.com/blog/threat-hunting-with-kubernetes-audit-logs/)

## Falco
- [awesome-falco](https://github.com/developer-guy/awesome-falco)
- [Analyze Falco Logs from K3S Cluster](https://github.com/developer-guy/falco-analyze-audit-log-from-k3s-cluster)
- [Analyze AWS EKS Audit logs with Falco](https://faun.pub/analyze-aws-eks-audit-logs-with-falco-95202167f2e)
- [Falco Sidekick](https://github.com/falcosecurity/falcosidekick)
- [Falco Driverkit with Docker on Debian](https://falco.org/blog/falco-driverkit-debian-docker/)
- [Restructuring the Kubernetes Threat Matrix and Evaluating Attack Detection by Falco](https://engineering.mercari.com/en/blog/entry/20220928-kubernetes-threat-matrix-and-attack-detection-by-falco/)
- [PCI/DSS Controls with Falco](https://falco.org/blog/falco-pci-controls/) - July '23

## Audit Logs
- [Audit Logs](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [Kubernetes Audit Logs | Use Cases & Best Practices](https://www.containiq.com/post/kubernetes-audit-logs) - July 2022
- [sysdig-cloud-scripts](https://github.com/draios/sysdig-cloud-scripts/tree/master/k8s_audit_config)

# Maintained Scanning Tools
- [kube-hunter](https://github.com/aquasecurity/kube-hunter)
- [kube-bench](https://github.com/aquasecurity/kube-bench)
- [kubaudit](https://github.com/Shopify/kubeaudit)
- [kubescape](https://github.com/armosec/kubescape) 
- [badrobot](https://github.com/controlplaneio/badrobot)
- [marvin](https://github.com/undistro/marvin)
- [managed kubernetes auditing toolkit](https://github.com/DataDog/managed-kubernetes-auditing-toolkit) - by DataDog

## SBOM
- [kubeclarity](https://github.com/openclarity/kubeclarity)
# Vulnerablities 
- [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat)

# Books
- [Hacking Kubernetes](https://www.oreilly.com/library/view/hacking-kubernetes/9781492081722/) - Martin & Hausenblas, October 2021

# Compliance
- [Elastic Compliant K8](https://elastisys.io/compliantkubernetes) - useful mapping of GDPR and ISO to Open Source projects

## PCI 
- [PCI Compliance for Containers and Kubernetes](https://sysdig.com/blog/container-pci-compliance/) - March 2020
- [Full Sail Ahead: Navigating PCI Compliance on Kubernetes - Part 1, Networking](https://www.schellman.com/blog/full-sail-ahead-part-1) 
- [PCI Compliance for Kubernetes in detail - Part 2 - Authorization](https://raesene.github.io/blog/2022/10/08/PCI-Kubernetes-Section2-Authorization/) - Oct 2022
