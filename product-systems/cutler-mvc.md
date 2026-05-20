# Minimally Viable Consistency (MVC) for Tool and Process Governance

When designing a mid-sized organization (100-200 people) that sits within a larger Corporate enterprise (5,000+ people) and operates across multiple states, properties, and regulatory frameworks, applying John Cutler's concept of **Minimally Viable Consistency (MVC)** is critical for balancing enterprise legibility with local agility.

The goal of MVC in this context is not to enforce monolithic standardization, but to define the *least amount of consistency required* to operate safely and effectively, without creating "performative compliance" (where teams do things one way in reality, while filling out official systems that don't help them).

## The Core Question: Viable for Whom?

When evaluating any proposed tool mandate or process standard, you must ask: **"Viable for whom?"**

Centralized leadership often demands consistency because it makes oversight, reporting, and governance easier. However, if that consistency forces local property teams to absorb massive friction, ignore local realities, or engage in "double work," it is not truly viable for the organization as a whole. 

**Design Principle:** The organization should absorb the complexity of the enterprise at the leadership/interface layer, rather than forcing every local team to adopt unnatural workflows just to satisfy Corporate reporting requirements.

---

## Applying the Three Approaches to Tools and Processes

To effectively govern tools and processes, categorize them using the three strategies of MVC:

### 1. Sharp Consistency (Strict Schemas)
This is where governance is non-negotiable, heavily audited, and centrally approved. This approach is reserved only for areas where the "translation tax" or enterprise risk of variation is unacceptably high.

*   **The Test:** *"If a team uses a different tool or process here, does it create financial, security, or regulatory risk for the enterprise?"*
*   **Examples:**
    *   **Core Security & Identity:** Single Sign-On (SSO), endpoint management, and core access policies.
    *   **Systems of Record:** The general ledger (Finance) and the core HRIS (e.g., Workday).
    *   **Enterprise-wide Risk:** Incident reporting for critical regulatory breaches that must flow immediately to Corporate legal.
*   **Governance Stance:** *"You must use this exact tool and follow this exact process. We do not support alternatives."*

### 2. Flexible Consistency (Shared Interfaces)
This is where mid-sized orgs often get bogged down by over-standardization. For many workflows, you do not need everyone to use the same tool; you just need to govern the *handoffs* and the *interfaces*.

*   **The Test:** *"Are we asking for consistent behaviors (e.g., 'everyone must use Jira exactly this way') when all we really need is a consistent interface (e.g., 'we need to know weekly project status')?"*
*   **Examples:**
    *   **Work/Task Management:** A software team might need a complex Jira setup, while a property maintenance team needs a lightweight mobile Kanban app. Don't force one tool; require that whatever tool is used can export standard status metrics to leadership.
    *   **Vendor Onboarding:** The intent (vetting and compliance) is consistent, but a state with strict environmental laws will have a heavier process than a state with loose laws. Let the process bend to the local need.
*   **Governance Stance:** *"We agree on the required outputs and security baselines. Bring your own tool or process, as long as it plugs into our required reporting/interface layer."*

### 3. Legible Variety (Named Inconsistencies)
In a multi-state, multi-property environment, standardizing certain processes actually destroys value because it ignores local reality. Legible variety means intentionally designing and explicitly naming the variations so the organization can navigate them.

*   **The Test:** *"Does this process need to bend to local physical or regulatory reality? If we force a standard process here, will the team just work around it in secret?"*
*   **Examples:**
    *   **State-Specific Compliance:** If State A requires a 3-step physical sign-off and State B requires zero, do not build a universal 3-step tool and force State B to click "N/A" constantly.
    *   **Property Operations:** The shift-handoff process for a massive resort property will structurally differ from a small satellite location.
*   **Governance Stance:** *"We acknowledge and document that Property A and Property B use fundamentally different tools and processes for this task. We have explicitly named these models (e.g., 'Strict-Reg Pods' vs. 'Standard Pods') so everyone understands why the differences exist."*

---

## Evaluation Checklist for New Tools and Processes

Before standardizing a new tool or mandating a new operational process, ask these questions:

1.  **Does this idea make people’s lives easier or harder at the local level?** 
    *   If it only benefits Corporate reporting but slows down local work, it is over-standardization.
2.  **What is the actual risk if this *wasn't* consistent?** 
    *   Be specific. Is it a regulatory/financial failure, or just a messy-looking spreadsheet for a VP? If the worst outcome is cosmetic inconsistency, the mandate is likely overkill.
3.  **Are there cheaper ways to achieve the consistency we want?** 
    *   Instead of a heavy mandate, could we provide a great template, a default tool, or shared visibility that nudges teams toward consistency naturally?
4.  **Is this a "Permanent Scaffold"?** 
    *   Are we introducing this process just to help a team learn a new skill or stabilize a chaotic situation? If so, put an expiration date on the mandate so it doesn't become permanent organizational drag.
5.  **What would it take to remove this later?** 
    *   Once a tool or process is embedded, it rarely disappears. If local regulations change next year, will this mandated tool be flexible enough to adapt, or will we be stuck with it?