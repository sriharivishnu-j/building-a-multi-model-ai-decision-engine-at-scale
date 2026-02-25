package main

import (
	"log"
	"net/http"
)

func dataIngestionHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("Received data ingestion request")
	w.Write([]byte("Data ingested successfully"))
}

func main() {
	http.HandleFunc("/ingest", dataIngestionHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}