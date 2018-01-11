import React from 'react';
import ReactDom from 'react-dom'

import { browserHistory, Router } from 'react-router';
import routes from './routes';

ReactDom.render(
  // eslint-disable-next-line
  <Router history={browserHistory} routes={routes} />, document.getElementById('root')
);
