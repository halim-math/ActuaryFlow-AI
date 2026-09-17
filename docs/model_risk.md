# Model risk management

ActuaryFlow-AI combines several model classes with different failure modes: retrieval ranking, language generation, deterministic actuarial formulas, statistical models, and routing thresholds. They should not be governed as one opaque component.

For each component record purpose, owner, inputs, outputs, assumptions, implementation version, validation evidence, known limitations, monitoring metrics, change approvals, and retirement criteria.

## Independent validation questions

- Is the component appropriate for the stated use?
- Are training/reference data representative of the use population and period?
- Are assumptions and transformations reproducible?
- Does performance remain acceptable under stress cases and distribution shift?
- Are failures detectable before they cause a consequential decision?
- Can a reviewer reconstruct what evidence and calculation produced an output?

Language-model fluency must not be treated as evidence of calibration or actuarial validity.
