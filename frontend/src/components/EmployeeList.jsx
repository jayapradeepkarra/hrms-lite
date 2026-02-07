import { useEffect, useState } from "react";
import api from "../services/api";

export default function EmployeeList({ refresh }) {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchEmployees = async () => {
    try {
      const res = await api.get("/employees");
      setEmployees(res.data);
    } catch (err) {
      console.error("Failed to load employees", err);
    } finally {
      setLoading(false);
    }
  };

  const deleteEmployee = async (employeeId) => {
    if (!window.confirm("Delete this employee?")) return;

    await api.delete(`/employees/${employeeId}`);
    fetchEmployees();
  };

  useEffect(() => {
    fetchEmployees();
  }, [refresh]);

  if (loading) return <p>Loading employees...</p>;

  if (employees.length === 0)
    return <p className="empty-state">No employees found</p>;

  return (
    <table>
      <thead>
        <tr>
          <th>Employee ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Department</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {employees.map((emp) => (
          <tr key={emp.id}>
            <td>{emp.employee_id}</td>
            <td>{emp.full_name}</td>
            <td>{emp.email}</td>
            <td>{emp.department}</td>
            <td>
              <button
                className="btn-danger"
                onClick={() => deleteEmployee(emp.employee_id)}
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
