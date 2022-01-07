import { SURVEYS } from "@/data";

const getSurvey = async (id) => {
  // eslint-disable-next-line no-constant-condition
  if (true) {
    // ADD ENV VAR TO TELL US TO USE THE REAL BACKEND OR NO
    return fetch(`http://127.0.0.1:8000/api/poll/${id}`, {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    }).then((response) => response.json());
  } else {
    return SURVEYS.find((survey) => survey.id === id);
  }
};

export { getSurvey };
