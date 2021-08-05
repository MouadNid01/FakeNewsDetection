import 'bootstrap/dist/css/bootstrap.min.css';
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import './App.css';
import { FactCheck } from './ReqHandler'

function App() {
  const styles = {
    width: "80%",
    marginLeft: "auto",
    marginRight: "auto",
    marginTop: "90px",
  }
  return (
    <Formik
      initialValues={{ title: '', text: '' }}
      validationSchema={Yup.object({
        title: Yup.string()
          .required('Required'),
        text: Yup.string()
          .required('Required'),
      })}
      onSubmit={(values, { setSubmitting }) => {
        setTimeout(() => {
          FactCheck(JSON.stringify(values))
          setSubmitting(false);
        }, 300);
      }}
    >
      <div className="App">
        <header className="App-header">
          <div className="test card" style={styles}>
            <h1 className="card-title" style={{ marginTop: "10px", textAlign: "center" }}>
              Fake News Detector </h1>
            <div className="card-body"  >
              <div className="container">
                <Form>
                  <div className="form-group">
                    <label htmlFor="title" className="labels">Title</label>
                    <Field
                      name="title"
                      type="text"
                      className="fields form-control"
                      placeholder="Title"
                      autoComplete="off"
                    />
                    <p style={{ color: "red", fontSize: "13px" }}>
                      <ErrorMessage name="title" />
                    </p>
                  </div>
                  <div className="form-group">
                    <label htmlFor="text" className="labels">Text</label>
                    <Field
                      as="textarea"
                      name="text"
                      className="fields form-control"
                      placeholder="Text"
                      autoComplete="off"
                      cols={40}
                      rows={10}
                    />
                    <p style={{ color: "red", fontSize: "13px" }}>
                      <ErrorMessage name="text" />
                    </p>
                  </div>
                  <div className="form-group" style={{ textAlign: "center" }}>
                    <button type="submit" className="btn my-btn">Check</button>
                  </div>
                </Form>
                <br />                
                  <div id='result'></div>
              </div>
            </div>
          </div>
        </header>
      </div>
    </Formik>
  );
}

export default App;
