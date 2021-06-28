import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    int maxValue = 900;
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
            Container(
              color: Colors.red,
              width: 100,
              height: 100,
              padding: EdgeInsets.all(8.0),
              margin: EdgeInsets.all(8.0),
              alignment: Alignment.center,
              child: Text(
                '$_counter',
                style: Theme.of(context).textTheme.headline4,
              ),
            ),
            Container(
              color: Colors.green[200],
              width: 100,
              height: 100,
              padding: EdgeInsets.all(8.0),
              margin: EdgeInsets.all(8.0),
            ),
            Container(
              color: Colors.blue[200],
              width: 100,
              height: 100,
              padding: EdgeInsets.all(8.0),
              margin: EdgeInsets.all(8.0),
            ),
            SingleChildScrollView(
              padding: EdgeInsets.all(10.0),
              scrollDirection: Axis.horizontal,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                mainAxisSize: MainAxisSize.max,
                children: <Widget>[
                  Card(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                    elevation: 5.0,
                    child: Container(
                      color: Colors.cyan[maxValue],
                      width: 100,
                      height: 100,
                      padding: EdgeInsets.all(8.0),
                      margin: EdgeInsets.all(8.0),
                      alignment: Alignment.center,
                      child: Text(
                        "1",
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 50,
                        ),
                      ),
                    ),
                  ),
                  Container(
                    color: Colors.cyan[maxValue - 100],
                    width: 100,
                    height: 100,
                    padding: EdgeInsets.all(8.0),
                    margin: EdgeInsets.all(8.0),
                    alignment: Alignment.center,
                    child: Text(
                      "2",
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 50,
                      ),
                    ),
                  ),
                  Container(
                    color: Colors.cyan[maxValue - 200],
                    width: 100,
                    height: 100,
                    padding: EdgeInsets.all(8.0),
                    margin: EdgeInsets.all(8.0),
                    alignment: Alignment.center,
                    child: Text(
                      "3",
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 50,
                      ),
                    ),
                  ),
                  Container(
                    color: Colors.cyan[maxValue - 300],
                    width: 100,
                    height: 100,
                    padding: EdgeInsets.all(8.0),
                    margin: EdgeInsets.all(8.0),
                    alignment: Alignment.center,
                    child: Text(
                      "4",
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 50,
                      ),
                    ),
                  ),
                  Container(
                    color: Colors.cyan[maxValue - 400],
                    width: 100,
                    height: 100,
                    padding: EdgeInsets.all(8.0),
                    margin: EdgeInsets.all(8.0),
                    alignment: Alignment.center,
                    child: Text(
                      "5",
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 50,
                      ),
                    ),
                  ),
                  Container(
                    color: Colors.cyan[maxValue - 500],
                    width: 100,
                    height: 100,
                    padding: EdgeInsets.all(8.0),
                    margin: EdgeInsets.all(8.0),
                    alignment: Alignment.center,
                    child: Text(
                      "6",
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 50,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
