import AttendanceForm from "../components/AttendanceForm";
import AttendanceList from "../components/AttendanceList";

export default function Attendance() {
  return (
    <>
      <h2 className="page-title">Attendance Management</h2>

      <div className="attendance-grid">
        <div className="card">
          <h3 className="section-title">Mark Attendance</h3>
          <AttendanceForm />
        </div>

        <div className="card">
          <h3 className="section-title">Attendance Records</h3>
          <AttendanceList />
        </div>
      </div>
    </>
  );
}
