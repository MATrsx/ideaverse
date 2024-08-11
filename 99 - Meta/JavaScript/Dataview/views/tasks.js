function render({ type, scope, onDate, forceFormat }) {
  return app.utils.dataview.tasks.render({ dv, type, scope, onDate, forceFormat })
}

render(input);
