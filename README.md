# Prozessmodell-des-Firmware-Update-Workflows

# Firmware Update Process (BPMN + Version Check Script)

**Author:** Shuwen Yang

This demo shows how a **firmware update workflow** can be modeled with BPMN 
and supported by a small **Python script** for version analysis.  
The process includes flashing the Rootfs, checking MPC/MCU versions, 
and verifying the application version before releasing the device.  

- **BPMN model**: firmware_update.mmd (Mermaid flowchart)  
- **Python script**: `parse_versions.py` – reads `devices.csv`, 
  generates a mismatch list (`out/mismatch.csv`) 
  and a summary chart (`out/summary.png`).  

This project demonstrates practical skills in **process modeling (BPMN)**, 
**data analysis (Python, Pandas)**, and **automation** – 
relevant for technical consulting roles.
