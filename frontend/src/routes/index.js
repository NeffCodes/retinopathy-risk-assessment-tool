import { Route, Routes } from 'react-router-dom';
import { App } from '../base_app';

// Pages
import Login from '../components/Login';
import Register from '../components/Register';

const routes = (
  <Routes>
    <Route exact path="/" element={<App/>}>
      <Route path="accounts/login" element={<Login />} />
      <Route path="accounts/signup" element={<Register />} />
      <Route path="*" render={() => <h1>404 Not Found</h1>} />
    </Route>
  </Routes>
)

export default routes;
