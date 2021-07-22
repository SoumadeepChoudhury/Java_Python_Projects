package soumadeep;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.Date;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JTextField;

public class Application implements ActionListener {
	static JTextField text;
	static JProgressBar bar;
	static JButton button;
	static JLabel label2;
	static JButton but;

	public Application() {

		// Application Development
		ImageIcon n = new ImageIcon("Java_Program\\res\\Penguins.jpg");

		JFrame frame = new JFrame("Date To Day Finder");
		JLabel label = new JLabel("Welcome to DATE_DAY Finder");
		JLabel label1 = new JLabel("Enter date in dd/mm/yyyy format: ");
		label2 = new JLabel();
		label2.setVisible(false);
		bar = new JProgressBar(0, 100);
		bar.setValue(0);
		button = new JButton("Find Day");
		but = new JButton("CLEAR");
		but.setPreferredSize(new Dimension(80, 25));
		bar.setStringPainted(true);
		bar.setBounds(0, 0, 500, 300);
		bar.setVisible(false);
		bar.setForeground(Color.green);
		bar.setPreferredSize(new Dimension(400, 20));
		button.addActionListener(this);
		but.addActionListener(this);
		but.setFocusable(false);
		button.setFocusable(false);
		text = new JTextField(10);
		Date date = new Date();
		@SuppressWarnings("deprecation")
		String x = "" + date.getDate();
		@SuppressWarnings("deprecation")
		String x1 = "" + (date.getMonth() + 1);
		@SuppressWarnings("deprecation")
		String x2 = "" + (date.getYear() + 1900);
		if (x.length() == 1)
			x = "0" + x;
		if (x1.length() == 1)
			x1 = "0" + x1;
		text.setText(x + "/" + x1 + "/" + x2);
		text.addKeyListener(new KeyAdapter() {
			public void keyTyped(KeyEvent e) {
				if (text.getText().length() > 9)
					e.consume();
			}
		});

		Font fonts = new Font("MV Boli", Font.BOLD, 29);
		label.setFont(fonts);
		label1.setFont(new Font("Arial", Font.PLAIN, 20));
		label.setForeground(Color.magenta);
		label1.setForeground(Color.red);
		label.setBackground(Color.cyan);
		label2.setFont(new Font("Comic Sans MS", Font.BOLD, 40));
		label2.setForeground(Color.red);
		label2.setBackground(Color.cyan);
		JPanel panel = new JPanel();
		JPanel panel1 = new JPanel();
		JPanel panel2 = new JPanel();
		JPanel panel3 = new JPanel();
		panel1.setBackground(Color.cyan);
		panel2.setBackground(Color.cyan);
		panel3.setBackground(Color.cyan);
		panel3.add(label2);
		panel2.add(bar);
		panel1.add(label1);
		panel.add(label);
		panel.add(panel1);
		panel.add(text);
		panel.add(button);
		panel.add(panel2);
		panel.add(panel3);
		panel.add(but);
		panel.setBackground(Color.cyan);
		frame.add(panel);
		frame.setIconImage(n.getImage());
		frame.setSize(500, 300);
		frame.setLocationRelativeTo(null);
		frame.setVisible(true);
		frame.setResizable(false);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {

		new Application();

	}

	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == button) {
			bar.setString(null);
			String s = text.getText();
			int d1 = 0;
			int d = Integer.parseInt(s.substring(0, 2));
			int m = Integer.parseInt(s.substring(3, 5));
			int y = Integer.parseInt(s.substring(6));
			if (text.getText() == null)
				label2.setText("Enter data.");
			else {
				if ((s.charAt(1) <= 48 && s.charAt(1) >= 57) || (s.charAt(4) <= 48 && s.charAt(4) >= 57)
						|| (s.charAt(0) <= 48 && s.charAt(0) >= 57) || (s.charAt(3) <= 48 && s.charAt(3) >= 57)
						|| (s.charAt(6) <= 48 && s.charAt(6) >= 57) || (s.charAt(7) <= 48 && s.charAt(7) >= 57)
						|| (s.charAt(8) <= 48 && s.charAt(8) >= 57) || (s.charAt(9) <= 48 && s.charAt(9) >= 57))
					label2.setText("Enter valid data");

				if (d > 31 || m > 12) {
					label2.setVisible(false);
					label2.setText("Enter valid data");
				} else if (y % 4 != 0 && m == 2 && d > 28) {
					label2.setVisible(false);
					label2.setText("Enter valid data");
				} else if (y % 4 == 0 && m == 2 && d > 29) {
					label2.setVisible(false);
					label2.setText("Enter valid data");
				} else if ((y % 4 != 0) || ((y % 100) == 0 && (y % 400) != 0)) {
					label2.setVisible(false);
					int month[] = { 0, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6 };
					String day[] = { "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" };
					int year[] = { 6, 4, 2, 0 };
					d1 = (d + month[m] + year[(y / 100) % 4] + (y % 100) + ((y % 100) / 4)) % 7;
					label2.setText("     " + day[d1] + "     ");
				} else if (((y % 100) == 0 && (y % 4) == 0 && (y % 400) == 0) || ((y % 100) != 0 && (y % 4) == 0)) {
					label2.setVisible(false);
					;
					int x = 0;
					int month[] = { 0, 3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3 };
					String day[] = { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };
					int year[] = { 0, 5, 3, 1 };
					d1 = (((y % 100) - 1) / 4 * 2) + (((y % 100) - 1) - (((y % 100) - 1) / 4));
					if (d1 >= 7)
						d1 %= 7;
					for (int i = 1; i < m; i++) {
						x += month[i];
						if (x >= 7)
							x %= 7;
						d1 += x;
					}
					if (d >= 7)
						d1 += d % 7;
					else
						d1 += d;
					d1 += year[(y / 100) % 4];
					if (d1 >= 7)
						d1 %= 7;
					label2.setText("     " + day[d1] + "     ");
				}
			}
			new Thread(new Runnable() {
				@Override
				public void run() {
					bar.setVisible(true);
					text.setEditable(false);
					int count = 0;
					try {

						while (count <= 100) {
							bar.setValue(count);
							bar.repaint();
							if (count == 100) {
								text.setEditable(true);
								label2.setVisible(true);
							}
							Thread.sleep(25);
							count += 1;
						}
					} catch (InterruptedException e1) {
						e1.printStackTrace();
					}

					bar.setString("Completed Loading");
				}
			}).start();

		} else if (e.getSource() == but) {
			label2.setText(null);
			bar.setVisible(false);
			text.setText(null);
		} else
			bar.setVisible(false);
	}

}
