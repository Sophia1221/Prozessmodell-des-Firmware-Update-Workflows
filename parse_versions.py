#!/usr/bin/env python3
# <= 50 lines mini script
import pandas as pd, matplotlib.pyplot as plt, os, sys

def main(csv_path="devices.csv", outdir="out"):
    os.makedirs(outdir, exist_ok=True)
    df = pd.read_csv(csv_path, dtype=str).fillna("")
    # 标记达标
    df["ok"] = (df["current_version"] == df["target_version"])
    # 导出未达标清单
    mismatches = df[~df["ok"]].copy()
    mismatches.to_csv(os.path.join(outdir, "mismatch.csv"), index=False)
    # 统计
    counts = df["ok"].value_counts().rename(index={True:"Up-to-date", False:"Outdated"})
    # 画柱状图
    plt.figure()
    counts.reindex(["Up-to-date","Outdated"]).plot(kind="bar")
    plt.title("Devices status vs. target version")
    plt.ylabel("Count"); plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "summary.png"), dpi=150)
    print(f"Done. {len(df)} devices -> {len(mismatches)} need update.")
    print(f"Outputs: {outdir}/mismatch.csv, {outdir}/summary.png")

if __name__ == "__main__":
    csv = sys.argv[1] if len(sys.argv) > 1 else "devices.csv"
    main(csv)