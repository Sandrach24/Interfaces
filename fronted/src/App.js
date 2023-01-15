import logo from './logo.svg';
import './App.css'
import { Button } from 'semantic-ui-react'
import { Navigation } from './routes/Navigation';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navigation />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div><Button class="ui primary button">Primary</Button><Button class="ui secondary button">Secondary</Button></div>
      </header>
    </div>
  );
}

export default App;
