package main

import "net"
import "fmt"
// import "bufio"
import "os"

func main() {

  conn, err := net.Dial("tcp", "127.0.0.1:8088")
  // connect to this socket
  if err != nil {
      fmt.Printf("connect error:%s\n", err.Error())
      os.Exit(1)
  }
  text := "GET / HTTP/1.1\r\n" +
        "Host: bing.com\r\n" +
        "\r\n" +
        "baedfjoewoieiowoeiw"
  max := 2
  for i := 0; i < max; i++ {
    // read in input from stdin
    // reader := bufio.NewReader(os.Stdin)
    // text, _ := reader.ReadString('\n')
    // send to socket
    fmt.Fprintf(conn, text)
    // listen for reply
    message := make([]byte, 1024)
    // message, err := bufio.NewReader(conn).ReadString('\n')
    _, err = conn.Read(message)
    if err != nil {
        fmt.Printf("read from tcp, get error:%s\n", err.Error())
        break
    }
    fmt.Printf("Message from server: %s\n", string(message))
  }
  conn.Close()
}
