function changeInputs() {
  var selectedStory = document.getElementById("story-select").value;
  var inputFieldsDiv = document.getElementById("input-fields");

  inputFieldsDiv.innerHTML = ""; // Clear previous input fields

  if (selectedStory === "story1") {
    inputFieldsDiv.innerHTML = `
      <label for="noun">Noun:</label>
      <input type="text" id="noun" placeholder="Enter a noun">
      
      <label for="verb">Verb:</label>
      <input type="text" id="verb" placeholder="Enter a verb">
    `;
  } else if (selectedStory === "story2") {
    inputFieldsDiv.innerHTML = `
      <label for="animal">Animal:</label>
      <input type="text" id="animal" placeholder="Enter an animal">
      
      <label for="place">Place:</label>
      <input type="text" id="place" placeholder="Enter a place">
    `;
  } else if (selectedStory === "story3") {
    inputFieldsDiv.innerHTML = `
      <label for="color">Color:</label>
      <input type="text" id="color" placeholder="Enter a color">
      
      <label for="food">Food:</label>
      <input type="text" id="food" placeholder="Enter a food">
    `;
  }
}
function generateStory() {
  var selectedStory = document.getElementById("story-select").value;
  var story = "";

  if (selectedStory === "story1") {
    var noun = document.getElementById("noun").value;
    var verb = document.getElementById("verb").value;

    story = "Once upon a time, there was a " + noun + " who loved to " + verb + ".";
  } else if (selectedStory === "story2") {
    var animal = document.getElementById("animal").value;
    var place = document.getElementById("place").value;

    story = "In a " + place + ", there was a " + animal + " roaming freely.";
  } else if (selectedStory === "story3") {
    var color = document.getElementById("color").value;
    var food = document.getElementById("food").value;

    story = "The " + color + " sky was filled with the aroma of " + food + ".";
  }
  
  document.getElementById("story").innerText = story;
}
