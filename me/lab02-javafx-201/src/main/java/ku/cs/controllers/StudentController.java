package ku.cs.controllers;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import ku.cs.models.Student;

public class StudentController {
    @FXML Label nameLabel;
    @FXML Label idLabel;
    @FXML Label scoreLabel;

    @FXML
    public void initialize() {
        Student student = new Student("6410400001", "Tony Stark");
        showStudent(student);
        student.addScore(100);
    }

    private void showStudent(Student student) {
        nameLabel.setText(student.getName());
        idLabel.setText(Student.getId());
        scoreLabel.setText(String.format(("%2.f",student.getScore())));
    }
}
