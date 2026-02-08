// import axios from "axios";

// // const api = axios.create({
// //   baseURL: "http://localhost:8000",
// //   headers: {
// //     "Content-Type": "application/json"
// //   }
// // });

// const api = axios.create({
//   baseURL: "https://hrms-lite-6uzn.onrender.com",
// });

// export default api;

import axios from "axios";

const api = axios.create({
  baseURL: "https://hrms-lite-6uzn.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: false, // IMPORTANT
});

export default api;


