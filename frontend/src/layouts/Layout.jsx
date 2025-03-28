import React from "react";
import { Outlet } from "react-router-dom";

import "../styles/layout.css";

export default function Layout() {
  return (
    <div className="layout">
      <header>
        <h1>QAP</h1>
      </header>
      <main>
        <Outlet />
      </main>
    </div>
  );
}
