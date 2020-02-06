import React, { useState } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';
import Navbar from './components/Appbar.js';
import CityList from './components/CityList.js';
import CityView from './components/CityView.js';
import { client } from './apollo.js';
import { ApolloProvider } from '@apollo/react-hooks';
import { BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import './App.css';


const useStateWithLocalStorage = localStorageKey => {
  const [city, setCurrentCity] = useState(
    (localStorage.hasOwnProperty(localStorageKey) && localStorage.getItem(JSON.parse(localStorageKey))) || { name: "Coruscant", slug: "coruscant", id: null}
  );
  React.useEffect(() => {
    localStorage.setItem(localStorageKey, JSON.stringify(city));
  }, [city]);
  return [city, setCurrentCity];
};

function App() {

  // const [city, setCurrentCity] = useStateWithLocalStorage(
  //   'currentCity'
  // );

  const [city, setCurrentCity] = useState({ name: "Coruscant", slug: "coruscant", id: null});

  return (
    <ApolloProvider client={client}>
      <CssBaseline />
      <Router>
        <div className="App">
          <Navbar city={city}/>
          <Container maxWidth="lg">
            <Switch>
              <Route path="/cities/:slug" component={CityView} />
              <Route exact path="/cities">
                <CityList setCurrentCity={setCurrentCity} currentCity={city}/>
              </Route>
              <Route path="/users">
                <p>This is the route content users</p>
              </Route>
              <Route exact path="/">
                <p>This is the route content home</p>
              </Route>
            </Switch>
          </Container>
        </div>
      </Router>
    </ApolloProvider>
  );
}

export default App;
