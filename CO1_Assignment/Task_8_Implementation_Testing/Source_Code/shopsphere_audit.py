from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "Task_9_Experimental_Performance"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SERVER_OPS_PER_SECOND = 100_000_000
SIZES = [100_000, 1_000_000]

def m1_pairs(n):
    return n * (n - 1) // 2

def m2_audits(n):
    if n <= 1:
        return 0
    return 2 ** math.ceil(math.log2(n)) - 1

def s2_levels(n):
    if n <= 0:
        return 0
    return math.ceil(math.log2(n + 1))

def m4_current(n):
    # Exact recurrence count for powers of two, T(1)=1.
    k = round(math.log2(n))
    if n == 2 ** k:
        return 2 * n * n - n
    # Recurrence-level estimate for other n.
    return int(2 * n * n)

def m4_redesign(n):
    # Exact for powers of two, T(1)=1; approximate otherwise.
    k = round(math.log2(n))
    if n == 2 ** k:
        return n * k + n
    return int(n * math.log2(n) + n)

def m5_estimate(n):
    # Recurrence-level estimate; exact formula applies when n is a power of two.
    k = math.log2(n)
    return int(n * (1 + k * (k + 1) / 2))

def report_generator(n):
    return int(3 * n * n + 10 * n * math.log2(n) + 50)

rows = []
for n in SIZES:
    modules = [
        ("M1 Duplicate Listing", m1_pairs(n)),
        ("M2 API Rate Limiter", m2_audits(n)),
        ("M3 S2 Binary Search", s2_levels(n)),
        ("M4 Current", m4_current(n)),
        ("M4 Proposed", m4_redesign(n)),
        ("M5 Sales Analytics", m5_estimate(n)),
        ("Report Generator", report_generator(n)),
    ]
    for module, operations in modules:
        rows.append({
            "module": module,
            "n": n,
            "estimated_operations": operations,
            "estimated_seconds_at_1e8_ops_per_second":
                operations / SERVER_OPS_PER_SECOND,
            "within_600_seconds_under_model":
                operations / SERVER_OPS_PER_SECOND <= 600,
            "measurement_type": "theoretical operation-count estimate, not measured runtime"
        })

csv_path = OUTPUT_DIR / "operation_estimates.csv"
with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("ShopSphere operation-count audit")
print("Assumed server rate:", f"{SERVER_OPS_PER_SECOND:,}", "operations/second")
print("Nightly window: 600 seconds")
print("-" * 90)
for row in rows:
    print(
        f"{row['module']:24s} n={row['n']:>9,} "
        f"ops={row['estimated_operations']:>18,} "
        f"time={row['estimated_seconds_at_1e8_ops_per_second']:>12.6f}s "
        f"within_window={row['within_600_seconds_under_model']}"
    )
print("\nCSV saved to:", csv_path)

try:
    import matplotlib.pyplot as plt
    graph_dir = ROOT / "Report" / "Tables_and_Graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)
    for module in sorted(set(r["module"] for r in rows)):
        module_rows = [r for r in rows if r["module"] == module]
        xs = [r["n"] for r in module_rows]
        ys = [r["estimated_seconds_at_1e8_ops_per_second"] for r in module_rows]
        plt.plot(xs, ys, marker="o", label=module)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input size n (log scale)")
    plt.ylabel("Estimated time in seconds (log scale)")
    plt.title("ShopSphere theoretical operation-count estimates")
    plt.legend(fontsize="small")
    plt.grid(True, which="both", linestyle=":")
    plt.tight_layout()
    graph_path = graph_dir / "estimated_time_scaling.png"
    plt.savefig(graph_path, dpi=180)
    plt.close()
    print("Graph saved to:", graph_path)
except ImportError:
    print("Matplotlib not installed; skipping graph.")
    print("Install it with: python -m pip install matplotlib")
