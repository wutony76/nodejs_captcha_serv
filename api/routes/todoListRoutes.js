'use strict';

module.exports = function(app) {
  var todoList = require('../controllers/todoListController');

  // todoList Routes
  app.route('/').get(todoList.test);
      // .post(todoList.create_a_task);

  app.route('/parse')
    .get(todoList.parse)
    .post(todoList.parse);

    // app.route('/tasks/:taskId')
    //     .get(todoList.read_a_task)
    //     .put(todoList.update_a_task)
    //     .delete(todoList.delete_a_task);
};