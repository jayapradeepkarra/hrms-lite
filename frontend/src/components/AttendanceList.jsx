import { useState } from "react";
import api from "../services/api";

export default function AttendanceList() {
  const [employeeCode, setEmployeeCode] = useState("");
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [searched, setSearched] = useState(false);

  const fetchAttendance = async () => {
    if (!employeeCode.trim()) {
      setError("Please enter Employee ID");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setSearched(true);

      const res = await api.get(`/attendance/${employeeCode}`);
      setRecords(res.data);
    } catch (err) {
      setError("Failed to fetch attendance");
      setRecords([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="filter-row">
        <input
          placeholder="Employee ID (e.g. EMP001)"
          value={employeeCode}
          onChange={(e) => setEmployeeCode(e.target.value)}
        />
        <button onClick={fetchAttendance}>
          {loading ? "Loading..." : "View"}
        </button>
      </div>

      {error && (
        <div className="empty-state" style={{ color: "red" }}>
          {error}
        </div>
      )}

      {!loading && searched && records.length === 0 && !error && (
        <div className="empty-state">
          No attendance records found
        </div>
      )}

      {!loading && records.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Employee ID</th>
              <th>Employee Name</th>
              <th>Date</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {records.map((r) => (
              <tr key={r.id}>
                <td>{r.employee_code}</td>
                <td>{r.employee_name}</td>
                <td>{r.date}</td>
                <td
                  className={
                    r.status === "Present"
                      ? "status-present"
                      : "status-absent"
                  }
                >
                  {r.status}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </>
  );
}
