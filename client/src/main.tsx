import { Router } from "@solidjs/router";
import { render } from "solid-js/web";

import App from "./App";
import "./index.css";

render(
  () => (
    <Router>
      <App />
    </Router>
  ),
  document.getElementById("root") as HTMLElement
);
