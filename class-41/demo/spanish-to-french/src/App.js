import React from 'react'
import './App.css';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      mainMessage: "Hola Mundo"
    }
    this.frenchClicked = this.frenchClicked.bind(this);
  }

  frenchClicked() {
    this.setState({
        mainMessage: "Bonjour Monde"
    })
  }
  render() {
    return (
      <div className="App">
        <Header title="Spanish to French" />
        <Main text={this.state.mainMessage} />
        <button onClick={this.frenchClicked}>Translate</button>
        <Footer message="I turn Spanish into French" />
      </div>
    );
  }
}

function Header(props) {
  return (
      <nav>
          <h2>{props.title}</h2>
      </nav>
  )
}

function Main(props) {
  return (
      <>
        <h1>Spanish to French</h1>
        <p>{props.text}</p>
      </>
  )
}

function Footer(props) {
    return (
        <footer>
            <p>{props.message}</p>
        </footer>
    )
}

export default App;
