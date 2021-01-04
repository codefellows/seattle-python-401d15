import React from "react";

export default class CreateEntryForm extends React.Component {
  constructor(props) {
    super(props);
    this.submitHandler = this.submitHandler.bind(this);
  }

  submitHandler(event) {
    event.preventDefault();
    this.props.onSubmit({
        resource:"snacks",
        base: "https://snacks-circle-back.herokuapp.com",
        username:"jb",
        password:"jb",
     });
  }


  render() {
    return (
      <>
        <h2>Fake Form</h2>
        <p>Hard Code your values for now</p>
        <button onClick={this.submitHandler}>SUBMIT</button>
      </>
    );
  }
}
