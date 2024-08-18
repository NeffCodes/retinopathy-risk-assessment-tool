import { Route, Routes } from 'react-router-dom';
import { App } from '../base_app';

// Pages
import { Login, Register } from '../components/auth';

const routes = (
  <Routes>
    <Route exact path="/" element={<App/>}>
      <Route path="login" element={<Login />} />
      <Route path="register" element={<Register />} />
    </Route>
    <Route path="*" render={() => <h1>404 Not Found</h1>} />
  </Routes>
)

export default routes;
