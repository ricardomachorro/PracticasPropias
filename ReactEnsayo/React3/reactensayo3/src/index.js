/*import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './componentes/App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();*/
import React from 'react';
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { createStore, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
import rootReducer from './reducers'

import './index.css';
import AppComponent from './componentes/App';

let store = createStore(
  rootReducer,
  applyMiddleware(thunk)
);

render(
  <Provider store={store}>
    <AppComponent />
  </Provider>,
  document.getElementById('root')
)
