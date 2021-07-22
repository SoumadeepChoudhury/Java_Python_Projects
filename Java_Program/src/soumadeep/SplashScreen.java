package soumadeep;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;

public class SplashScreen {

	public static void main(String[] args) {
		ImageIcon img = new ImageIcon("Java_Program\\res\\image.jpg");
		JFrame frame = new JFrame();
		JProgressBar bar = new JProgressBar();
		JLabel label = new JLabel(img);
		JLabel label1 = new JLabel("WELCOME");
		label1.setFont(new Font("MS Boli", Font.BOLD, 30));
		label1.setForeground(Color.red);
		JPanel panel = new JPanel();
		panel.setBackground(Color.black);
		bar.setVisible(false);
		bar.setPreferredSize(new Dimension(400, 7));
		panel.add(label);
		panel.add(label1);
		panel.add(bar);
		bar.setLocation(10, 10);
		bar.setForeground(Color.green);
		bar.setBackground(Color.white);

		new Thread(new Runnable() {
			@Override
			public void run() {
				for (double i = 0; i < 1000000000.0; i++)
					;
				bar.setVisible(true);
				int count = 0;
				try {

					while (count <= 100) {
						bar.setValue(count);
						bar.repaint();
						if (count == 50)
							for (double i = 0.0; i < 1000000000.0; i++)
								;
						if (count == 100) {
							frame.dispose();
							Application.main(null);
						}
						Thread.sleep(40);
						count += 1;
					}
				} catch (InterruptedException e1) {
					e1.printStackTrace();
				}

			}
		}).start();
		frame.getContentPane().add(panel);
		frame.getContentPane().setBackground(Color.black);
		frame.setSize(400, 270);
		frame.setLocationRelativeTo(null);
		frame.setUndecorated(true);
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}
}