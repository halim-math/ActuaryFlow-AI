# Privacy by design

Insurance workflows can contain personal and financial information. The reference architecture therefore minimizes data collection and separates operational identifiers from model prompts where practical.

Recommended controls include purpose limitation, explicit retention periods, tenant isolation, encryption in transit and at rest, role-based access, deletion workflows, secret redaction, prompt/log minimization, data-processing inventories, and incident response procedures.

Avoid placing unnecessary identifiers in vector indexes or long-lived conversational memory. Retrieval metadata should use surrogate document IDs when possible. Evaluation datasets should be synthetic or appropriately de-identified unless a governed basis exists for using production data.

A production operator remains responsible for determining applicable privacy obligations and lawful processing conditions in its jurisdiction.
