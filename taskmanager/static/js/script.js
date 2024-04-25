document.addEventListener("DOMContentLoaded", () => {
  initSidenav();
  initDatepicker();
  initSelect();
});

const initSidenav = () => {
  const sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav, {
    edge: 'left',
    inDuration: 250,
    outDuration: 200,
    draggable: true
  });
};

const initDatepicker = () => {
  const datepicker = document.querySelectorAll(".datepicker");
  const {
    Datepicker
  } = M;
  Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: {
      done: "Select"
    }
  });
};

const initSelect = () => {
  const selects = document.querySelectorAll("select");
  const {
    FormSelect
  } = M;
  FormSelect.init(selects);
};
