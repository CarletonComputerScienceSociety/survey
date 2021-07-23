const SURVEYS = [
  {
    id: 1,
    title: "Survey Test",
    questions: [
      {
        id: 1,
        order: 1,
        type: "MultipleChoiceQuestion",
        body: "Which of the following future events would you attend?",
        answers: [
          {
            id: 1,
            text: "Speed Friending",
          },
          {
            id: 2,
            text: "Tech Talk",
          },
          {
            id: 3,
            text: "Workshop",
          },
          {
            id: 4,
            text: "None of the above",
          },
        ],
      },
      {
        id: 2,
        order: 2,
        type: "MultipleChoiceQuestion",
        body: "What year standing are you?",
        answers: [
          {
            id: 1,
            text: "1st year",
          },
          {
            id: 2,
            text: "2nd year",
          },
          {
            id: 3,
            text: "3rd year",
          },
          {
            id: 4,
            text: "4th year",
          },
        ],
      },
      {
        id: 3,
        order: 3,
        type: "MultipleChoiceQuestion",
        body: "Would you attend another event hosted by the CCSS?",
        answers: [
          {
            id: 1,
            text: "Yes",
          },
          {
            id: 2,
            text: "No",
          },
        ],
      },
    ],
  },
];

export { SURVEYS };
