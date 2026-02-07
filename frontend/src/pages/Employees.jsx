import { useState } from "react";
import EmployeeForm from "../components/EmployeeForm";
import EmployeeList from "../components/EmployeeList";

export default function Employees() {
  const [refresh, setRefresh] = useState(false);

  return (
    <>
      <h2>Employee Management</h2>

      <div className="card">
        <EmployeeForm onSuccess={() => setRefresh(!refresh)} />
      </div>

      <div className="card">
        <EmployeeList refresh={refresh} />
      </div>
    </>
  );
}
