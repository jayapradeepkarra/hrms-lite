import { useState } from "react";
import api from "../services/api";


export default function EmployeeForm({ onSuccess }){

  const [form, setForm] = useState({
    employee_id: "",
    full_name: "",
    email: "",
    department: ""
  });

const submit = async (e) => {
  e.preventDefault();
 console.log("POSTING TO /employees/", form);
  await api.post("/employees/", form);
  onSuccess();     // 🔁 refresh list
  alert("Employee added successfully");
    setForm({ employee_id: "", full_name: "", email: "", department: "" });
};


  return (
    <form className="form-group" onSubmit={submit}>
      <input
        placeholder="Employee ID (EMP001)"
        value={form.employee_id}
        onChange={(e) =>
          setForm({ ...form, employee_id: e.target.value })
        }
        required
      />

      <input
        placeholder="Full Name"
        value={form.full_name}
        onChange={(e) =>
          setForm({ ...form, full_name: e.target.value })
        }
        required
      />

      <input
        type="email"
        placeholder="Email"
        value={form.email}
        onChange={(e) =>
          setForm({ ...form, email: e.target.value })
        }
        required
      />

      <input
        placeholder="Department"
        value={form.department}
        onChange={(e) =>
          setForm({ ...form, department: e.target.value })
        }
        required
      />

      <button>Add Employee</button>
    </form>
  );
}
