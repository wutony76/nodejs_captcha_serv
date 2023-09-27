'use strict';
const child = require('child_process');
child.exec ('node -v', function (err, sto) {
  console.log('node.ver', sto)
})
// child.exec ('python3 py/parseImg.py dddd', function (err, sto) {
//   console.log('check', sto, err)
// })

function command (cmd, cb) {
  child.exec (cmd, function (err, sto) {
    console.log('command.errs = ', err)
    cb(sto)
  })
}

exports.test = function (req, res) {
  console.log('test')
  res.send("HOME. Hellow ABC");
};

exports.parse = function (req, res) {
  console.log('parse', req.query.d)
  const d = req.query.d;
  if (!d) return { code: -1, msg: 'no can use data.'}

  let nodeVer = null 
  // const useCmd = 'node -v'
  const useCmd = `arch -arm64 python3 py/parseImg.py ${d}`
  // const useCmd = `python3 py/test.py ${url}`
  // const useCmd = `python3 py/parseImg.py`
  // const useCmd = `python3 py/parseImg.py ${url}`
  console.log('useCmd > ', useCmd)
  command(useCmd, (data) => {
    console.log('node', data)
    nodeVer = data
    console.log('data > ', data)

    const output = {
      code: 0,
      data: data,
      // node: nodeVer,
      msg: `PARSE > ${d}`
    }
    res.send(output);
  })
}

