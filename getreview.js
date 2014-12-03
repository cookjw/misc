/* Code from a Codecademy exercise that did exactly what was asked, but
was nevertheless not accepted by the tutorial. Figured I'd save it for
posterity, or in case I ever wanted an example of the phenomenon. */

var getReview = function (movie) {
  var reviewDict = {"Toy Story 2" : "Great story. Mean prospector.",
  "Finding Nemo": "Cool animation, and funny turtles.",
  "The Lion King" : "Great songs.",
  };
  for (var film in reviewDict) {
      if (movie === film) {
        return reviewDict[movie];  
      };
  };
  return "I don't know!";
};

getReview("Toy Story 2");
