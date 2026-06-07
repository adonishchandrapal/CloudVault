from pathlib import Path

def get_dashboard_data(upload_dir):

    files = [
        f for f in upload_dir.rglob("*")
        if f.is_file()
    ]

    folders = [
        f for f in upload_dir.rglob("*")
        if f.is_dir()
    ]

    total_size = sum(
        f.stat().st_size
        for f in files
    )

    return {
        "files": len(files),
        "folders": len(folders),
        "size_mb": round(
            total_size / (1024 * 1024),
            2
        )
    }