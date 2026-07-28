from fastapi import APIRouter, HTTPException
from backend.schemas import LoginRequest
from backend.database_manager import (
    get_all_jobs_with_results,
    delete_job,
    get_feedback_count
)

router = APIRouter()


@router.post("/login")
def admin_login(data: LoginRequest):
    # Temporary hardcoded admin credentials for the prototype
    # You can safely change these as long as the frontend login form
    # uses the same new username/password when you test.
    if data.username == "admin" and data.password == "FJPD_Admin_2026!":
        return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/records")
def get_records():
    records = get_all_jobs_with_results()

    formatted_records = []
    for row in records:
        formatted_records.append({
            "post_id": row[0],
            "title": row[1],
            "prediction": row[2],
            "confidence": row[3]
        })

    return formatted_records


@router.get("/stats")
def get_stats():
    records = get_all_jobs_with_results()

    total = len(records)
    fake = 0
    real = 0

    for row in records:
        prediction = str(row[2]).strip().lower() if row[2] is not None else ""

        if prediction == "fake":
            fake += 1
        elif prediction == "real":
            real += 1

    fake_rate = round((fake / total) * 100, 1) if total > 0 else 0.0
    feedback_count = get_feedback_count()

    return {
        "total": total,
        "fake_count": fake,
        "real_count": real,
        "fake_rate": fake_rate,
        "feedback_count": feedback_count
    }


@router.delete("/record/{record_id}")
def delete_record(record_id: int):
    delete_job(record_id)
    return {"message": f"Record {record_id} deleted successfully"}