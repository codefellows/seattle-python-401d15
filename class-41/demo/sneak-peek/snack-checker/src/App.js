import React from "react";
import "./App.css";
import FetchResourceForm from "./fetch-resource-form";
import fetchResource from "./Fetcher"
import SnackList from "./SnackList"

class App extends React.Component {
  constructor(props) {
    super(props);
    this.fetchSnacks = this.fetchSnacks.bind(this);
    this.state = {
      snacks: []
    };
  }

  async fetchSnacks(data) {

    const snacks = await fetchResource(data);

    this.setState({
      snacks
    });
  }

  render() {
    return (
      <div className="App">
        <h1>Snack Checker</h1>
        <FetchResourceForm onSubmit={this.fetchSnacks} />
        <SnackList snacks={this.state.snacks} />
      </div>
    );
  }
}

export default App;
