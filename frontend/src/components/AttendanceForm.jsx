import { useState } from "react";
import api from "../services/api";

export default function AttendanceForm() {
  const [form, setForm] = useState({
    employee_id: "",
    date: "",
    status: "Present"
  });

  const submit = async (e) => {
    e.preventDefault();
    await api.post("/attendance", form);
    alert("Attendance marked successfully");
    setForm({ employee_id: "", date: "", status: "Present" });
  };

  return (
    <form className="form-group" onSubmit={submit}>
      <input
        placeholder="Employee ID"
        value={form.employee_id}
        onChange={(e) =>
          setForm({ ...form, employee_id: e.target.value })
        }
        required
      />

      <input
        type="date"
        value={form.date}
        onChange={(e) =>
          setForm({ ...form, date: e.target.value })
        }
        required
      />

      <select
        value={form.status}
        onChange={(e) =>
          setForm({ ...form, status: e.target.value })
        }
      >
        <option>Present</option>
        <option>Absent</option>
      </select>

      <button>Submit</button>
    </form>
  );
}
