import { createTheme, responsiveFontSizes } from "@mui/material";

const baseTheme = responsiveFontSizes(
  createTheme({
    typography: {
      htmlFontSize: 16, // base font size used to calculate 1.0 REM
      h1: {
        fontFamily: "Roboto",
        fontStyle: "normal",
        fontWeight: 600,
        fontSize: "2.5rem",
        lineHeight: 1.4,
      },
      h2: {
        fontFamily: "Roboto",
        fontSize: "2.2rem",
      },
      h3: {
        fontFamily: "Roboto",
        fontSize: "1.8rem",
      },
      h4: {
        fontFamily: "Roboto",
        fontSize: "1.4rem",
      },
      subtitle1: {
        fontFamily: "Open Sans",
        fontStyle: "normal",
        fontWeight: 600,
        fontSize: 15,
        lineHeight: 20,
        color: "rgba(0, 0, 0, 0.38)",
      },
    },
    palette: {
    primary: {
      light: '#8561c5',
      main: '#673ab7',
      dark: '#482880',
      contrastText: '#fff',
    },
    secondary: {
      light: '#4aedc4',
      main: '#1de9b6',
      dark: '#14a37f',
      contrastText: '#000',
    },
    }
  })
);

export { baseTheme };