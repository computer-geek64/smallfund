import Navbar from './components/Navbar';
import Home from './components/Home';
import NewListing  from './components/NewListing';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
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
        <Router>
          <Navbar/>

          <Switch>

            <Route exact path="/">
              <Home/>
              <Home/>
            </Route>

            <Route path="/add">
              <NewListing/>
            </Route>

          </Switch>
        </Router>
      </div>
    </ThemeProvider>
  );
}

export default App;
