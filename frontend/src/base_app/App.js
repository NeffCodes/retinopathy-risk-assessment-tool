import React from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import { Box } from "@mui/material";

import LandingPage from './LandingPage';

const App = () => {
  const location = useLocation();

  let children = <Outlet />
  if (location.pathname === "/") {
    children = <LandingPage />;
  }

  return <Box>{children}</Box>
}

export default App;