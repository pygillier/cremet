import React from 'react';
import Navbar from './components/Appbar.js';
import CityList from './components/CityList.js';
import { client } from './apollo.js';
import { ApolloProvider } from '@apollo/react-hooks';
import { BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import './App.css';

function App() {
  return (
    <ApolloProvider client={client}>
      <Router>
        <div className="App">
          <Navbar/>
          <Switch>
          <Route path="/cities">
            <CityList/>
          </Route>
          <Route path="/users">
            <p>This is the route content users</p>
          </Route>
          <Route path="/">
            <p>This is the route content home</p>
          </Route>
        </Switch>
        </div>
      </Router>
    </ApolloProvider>
  );
}

export default App;
