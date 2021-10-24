import Main from './components/Main'
import NewListing  from './components/NewListing';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import './App.css';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <div className="App">
        <Main/>
        <NewListing/>
      </div>
    </ThemeProvider>
  );
}

export default App;
