# Office Artifact Manifest

The exact Office deliverables are stored in the designated Google Drive backup folder. GitHub contains the reviewable source, methodology, code, tests, templates, and a full Markdown edition of the handoff.

| Artifact | Bytes | SHA-256 | Source-controlled equivalent |
|---|---:|---|---|
| `Halo_Brand_Lift_Intern_Project_Handoff.docx` | 371,935 | `74129e1a646acf07b953a0cac4c6c4bdca5bb895db9dc5015e767ba3cfbea35a` | `docs/handoff/` and `docs/Halo_Analysis_Intern_Project_Handoff_Summary.md` |
| `Halo_Kickoff_and_Data_Intake.xlsx` | 28,443 | `35d0a88ea50bd98b02377a65f5269eb320ce07c7ae1e0428cc8bdf7953a67557` | `docs/WORKBOOK_GUIDE.md`, project templates, and calculation tests |
| `Halo_Project_Starter_Pack.zip` | 427,820 | `6f4f73943c5de1cd2d33e8a47523fd42acef96337c58796f30e6a989c87d4e65` | Snapshot of the complete starter package |

After downloading the Office files, verify them with:

```bash
python scripts/verify_office_artifacts.py /path/to/downloaded/folder
```

Do not commit client delivery data, raw extracts, credentials, or client-identifying exports to this public repository.
