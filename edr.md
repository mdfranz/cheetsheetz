# Case Studies

### LBL
- https://it.lbl.gov/countdown-to-sophos-end-of-life/
- https://it.lbl.gov/crowdstrike-falcon/

### Misc Universities
- https://tech.rochester.edu/services/antivirus-software/
- https://td.unh.edu/TDClient/60/Portal/KB/ArticleDet?ID=816
- https://its.uchicago.edu/epp/
- https://it.osu.edu/news/2023/05/19/how-crowdstrike-falcon-protects-university-devices
- https://confluence.som.yale.edu/display/SC/CrowdStrike+Frequently+Asked+Questions
- https://www.bu.edu/tech/services/cccs/desktop/device-security/endpoint-protection/

# Comparisions

## GitHub Repos
- https://github.com/tsale/EDR-Telemetry
- https://github.com/CyberSecurityUP/EDR-Assessment/

## Academic
- [An Empirical Assessment of Endpoint Security Systems Against Advanced Persistent Threats Attack Vectors](https://arxiv.org/pdf/2108.10422.pdf)

## Mitre - 2020

[21 Evals by Mitre](https://www.mitre.org/news-insights/news-release/mitre-releases-results-evaluations-21-cybersecurity-products)

- https://attackevals.mitre-engenuity.org/enterprise/participants/sentinelone?view=overview&adversary=wizard-spider-sandworm
- https://attackevals.mitre-engenuity.org/enterprise/participants/crowdstrike?view=overview&adversary=wizard-spider-sandworm

# Evasion
- [TA Phone Home: EDR Evasion Testing Reveals Extortion Actor's Toolkit](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/) - Nov 2024


# Testing

## EICAR

```
curl -o eicar.com https://secure.eicar.org/eicar.com
Invoke-WebRequest -Uri https://secure.eicar.org/eicar.com -OutFile eicar.com
```
or create a file with

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```
## Atomic Red Team
- https://www.atomicredteam.io/invoke-atomicredteam/docs
- [How to Run Atomic Red Team on Linux and Automate Attack Simulations with Velociraptor](https://socfortress.medium.com/how-to-run-atomic-red-team-on-linux-and-automate-attack-simulations-with-velociraptor-d4b52b05721b)
