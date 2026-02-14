# General
- [MCP Tools: Attack Vectors and Defense Recommendations for Autonomous Agents](https://www.elastic.co/security-labs/mcp-tools-attack-defense-recommendations)
- [A Security Engineer's Guide to MCP](https://semgrep.dev/blog/2025/a-security-engineers-guide-to-mcp/)
- [Avoiding MCP Mania | How to Secure the Next Frontier of AI](https://www.sentinelone.com/blog/avoiding-mcp-mania-how-to-secure-the-next-frontier-of-ai/)
- [Securing the Model Context Protocol](https://block.github.io/goose/blog/2025/03/31/securing-mcp/)
  > Explains how Block is securing its "goose" AI agent by focusing on secure communication, identity management, human-in-the-loop safety, and supply chain security.
- [The MCP Security Survival Guide: Best Practices, Pitfalls, and Real-World Lessons](https://towardsdatascience.com/the-mcp-security-survival-guide-best-practices-pitfalls-and-real-world-lessons/)
  > A deep dive into MCP threat models, real-world exploits, and architectural best practices, emphasizing strong authentication, input validation, and human approval.
- [Wiz MCP Security Briefing](https://www.wiz.io/blog/mcp-security-research-briefing)
  > Discusses the security implications of local and remote MCP servers and provides guidance for securing MCP adoption.
- [Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/pdf/2503.23278)
  > This paper systematically studies the Model Context Protocol (MCP) by defining its lifecycle, categorizing security threats, and proposing actionable safeguards for secure adoption.
- [Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies](https://arxiv.org/html/2504.08623v2)
  > This paper proposes enterprise-grade security frameworks and mitigation strategies to address novel security challenges introduced by the Model Context Protocol (MCP) for AI systems. 

# Tools
- [mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)
  > A security scanner for AI agents, MCP servers, and skills that detects vulnerabilities like prompt injection.
- [enact](https://github.com/EnactProtocol/specification)
  > A protocol for defining, discovering, and safely running AI-executable tools with cryptographic verification.
- [mcp-context-protector](https://github.com/trailofbits/mcp-context-protector) - see [blog](https://blog.trailofbits.com/2025/07/28/we-built-the-security-layer-mcp-always-needed/)
  > A security wrapper for MCP servers designed to mitigate risks like prompt injection from untrusted servers.
- [proximity](https://github.com/fr0gger/proximity)
  > A security scanner for MCP servers and Agent Skills that uses NOVA rules to identify prompt injection and jailbreak attempts.
- [Cisco mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
  > A Python tool that scans MCP servers and tools for security threats using YARA rules, LLM-as-a-judge, and other techniques.

# Authn/Authz

Integrating OAuth with MCP is complex and requires careful architectural consideration.

*   **Separation of Concerns**: The OAuth Authorization Server (AS) should be separate from the MCP server (acting as the Resource Server, RS). Coupling them increases complexity and violates enterprise best practices.
*   **Enterprise Integration**: The MCP Authorization spec can create friction with existing enterprise IdP and API gateway patterns. The recommended approach is for MCP servers to be stateless and delegate to existing IdPs.
*   **OAuth is Not Enough**: "Vanilla" OAuth does not address all MCP-related threats (e.g., replay attacks, fine-grained access control). It must be supplemented with other security measures.

* [OAuth's Role in MCP Security](https://defensiblesystems.substack.com/p/oauths-role-in-mcp-security)
* [Let's fix OAuth in MCP](https://aaronparecki.com/2025/04/03/15/oauth-for-model-context-protocol)
* [The MCP Authorization Spec Is... a Mess for Enterprise](https://blog.christianposta.com/the-updated-mcp-oauth-spec-is-a-mess/)
* [Piecing together the Agent puzzle: MCP, authentication & authorization, and Durable Objects free tier](https://blog.cloudflare.com/building-ai-agents-with-mcp-authn-authz-and-durable-objects/)
  > Details Cloudflare's enhancements to its Agents SDK for accelerating AI agent development, including new MCP capabilities, integrated auth providers, and making Durable Objects available on the free tier.

# Threats & Vulnerabilities

Several critical vulnerabilities have been found in real-world MCP implementations, demonstrating significant risks.

*   **EscapeRoute (CVE-2025-53109 & CVE-2025-53110)**: A sandbox escape in Anthropic's Filesystem MCP Server that allowed arbitrary file access and code execution through directory traversal and symlink manipulation.
*   **Slack MCP Server Data Leakage**: Anthropic's deprecated Slack MCP server was vulnerable to data exfiltration via prompt injection and Slack's "link unfurling" feature.
*   **MCP Inspector RCE (CVE-2025-49596)**: A Remote Code Execution vulnerability in Anthropic's MCP Inspector tool, caused by a lack of authentication and exploitable via CSRF from a malicious website.

* [Security Advisory: Anthropic's Slack MCP Server Vulnerable to Data Exfiltration](https://embracethered.com/blog/posts/2025/security-advisory-anthropic-slack-mcp-server-data-leakage/)
* [EscapeRoute: Breaking the Scope of Anthropic’s Filesystem MCP Server
(CVE-2025-53109 & CVE-2025-53110)](https://cymulate.com/blog/cve-2025-53109-53110-escaperoute-anthropic/)
* [Critical RCE in Anthropic MCP Inspector (CVE-2025-49596) Enables Browser-Based Exploits | Oligo Security](https://www.oligo.security/blog/critical-rce-vulnerability-in-anthropic-mcp-inspector-cve-2025-49596)
* [Cato CTRL™ Threat Research: PoC Attack Targeting Atlassian's Model Context Protocol (MCP) Introduces New “Living Off AI” Risk](https://www.catonetworks.com/blog/cato-ctrl-poc-attack-targeting-atlassians-mcp/)
  > Details a PoC attack where malicious input to Atlassian's MCP leads to prompt injection, allowing data exfiltration by leveraging internal users as proxies.
* [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
  > Explains how MCP is vulnerable to "rug pulls," "tool shadowing," and "tool poisoning" prompt injection attacks that can exfiltrate sensitive data.
* [The Permission Pitfall: Securing MCP Servers Without Limiting Value](https://www.joinformal.com/blog/the-permission-pitfall-securing-mcp-servers-without-limiting-value/)
  > Argues for a centralized agent permission control system to implement granular least-privilege access, addressing risks from insufficient authentication and authorization.
* [MCP Safety Audit: LLMs with the Model Context Protocol
Allow Major Security Exploits](https://arxiv.org/pdf/2504.03767) - Apr '25
  > This paper demonstrates that the MCP design enables major security exploits in LLM-powered systems and introduces the McpSafetyScanner tool to audit for these vulnerabilities.
* [MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
  > Describes "Tool Poisoning Attacks," where hidden malicious instructions in tool descriptions manipulate AI models into performing unauthorized actions.
* [Jumping the line: How MCP servers can attack you before you ever use them](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them) - Apr '25
  > Uncovers the "line jumping" vulnerability, where malicious MCP servers can execute attacks and manipulate model behavior before a tool is explicitly invoked.
