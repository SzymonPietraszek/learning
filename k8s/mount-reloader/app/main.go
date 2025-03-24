package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"path"
	"path/filepath"

	"github.com/fsnotify/fsnotify"
)

func ListDir(dirPath string) string {
	content, err := exec.Command("ls", "-al", dirPath).Output()
	if err != nil {
		return err.Error()
	}
	return fmt.Sprintf("Directory %s:\n%s", dirPath, string(content))
}

func ReadFile(filePath string) string {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return err.Error()
	}
	return fmt.Sprintf("File %s:\n\"\n%s\n\"\n", filePath, string(content))
}

func WatchChangesToMountedFile(log *log.Logger, mountPath string) {
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		log.Fatal(err)
	}
	defer watcher.Close()

	err = watcher.Add(path.Dir(mountPath))
	if err != nil {
		log.Fatal(err)
	}
	// because a mounted file is updated by kubernetes it is a symbolic
	// link and there will be no events with kubeconfig name. So we need to check if a target
	// file has changed.
	targetMountPath, _ := filepath.EvalSymlinks(mountPath)
	for {
		select {
		case event, ok := <-watcher.Events:
			if !ok {
				log.Println("event channel closed")
				return
			}
			log.Println("event:", event)
			newTargetMountPath, _ := filepath.EvalSymlinks(mountPath)
			if newTargetMountPath == targetMountPath {
				continue
			}
			targetMountPath = newTargetMountPath
			log.Print(ReadFile(mountPath))

			// HERE: your code to react on file changes

		case err, ok := <-watcher.Errors:
			if !ok {
				log.Println("error channel closed")
				return
			}
			log.Println("error:", err)
		}
	}
}

func main() {
	for mountType, mountPath := range map[string]string{
		"SECRET":      "/etc/secret-folder/data-from-secret",
		"CONFIG-MAP":  "/etc/configmap-folder/data-from-configmap",
		"ANNOTATIONS": "/etc/annotations/annotations-file",
	} {
		l := log.New(os.Stdout, mountType+": ", 0)
		l.Print(ListDir(path.Dir(mountPath)))
		l.Print(ReadFile(mountPath))
		go WatchChangesToMountedFile(l, mountPath)
	}

	// Block main goroutine forever.
	<-make(chan struct{})
}
