import customtkinter as ctk
import textwrap as tw
import Assets.PythonFiles.Variables as vary
import Assets.PythonFiles.GenerateReply as gr
from datetime import datetime as dt
from PIL import Image, ImageTk
from datetime import datetime


class MainWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry(f'{vary.width}x{vary.height}')
        self.iconbitmap('Assets/Images/icon.ico')
        self.title('ChatBot')
        self.resizable(0, 0)

        self.set_home_widgets()

    def set_home_widgets(self):
        # defining frames
        self.home_frame = ctk.CTkFrame(self, fg_color=vary.bg_clr)
        self.top_panel = ctk.CTkFrame(self.home_frame, fg_color=vary.bg_clr)
        self.chat_panel = ctk.CTkScrollableFrame(self.home_frame, fg_color=vary.chat_bg_clr, width=vary.width,
                                                 height=vary.height-130)
        self.bottom_panel = ctk.CTkFrame(self.home_frame, fg_color=vary.bg_clr, width=vary.width)

        # Defining icons
        self.img_1 = Image.open(f'Assets/Images/menu.png')
        self.res_img_1 = self.img_1.resize((20, 20))
        self.menu = ImageTk.PhotoImage(self.res_img_1)

        self.img_2 = Image.open(f'Assets/Images/icon_{vary.icon}.png')
        self.res_img_2 = self.img_2.resize((50, 50))
        self.dp = ImageTk.PhotoImage(self.res_img_2)

        self.img_3 = Image.open(f'Assets/Images/send.png')
        self.res_img_3 = self.img_3.resize((30, 30))
        self.send = ImageTk.PhotoImage(self.res_img_3)

        # defining labels
        self.chat_dp = ctk.CTkLabel(self.top_panel, fg_color=vary.bg_clr, text='', width=50, height=50, image=self.dp)
        self.chat_name = ctk.CTkLabel(
            self.top_panel, text=vary.bot_name, height=10, font=(vary.font_name, 22),
            text_color=vary.font_clr)
        self.date = ctk.CTkLabel(
            self.top_panel, text=dt.now().strftime('%B %d, %y'), height=10, font=(vary.font_name, 12),
            text_color=vary.font_clr)
        self.cheat_lbl = ctk.CTkLabel(self.chat_panel, text='', height=1, width=vary.width - 10)

        # defining text boxes
        self.input_field = ctk.CTkEntry(
            self.bottom_panel, width=vary.width-50, height=52, font=(vary.font_name, vary.font_size),
            fg_color=vary.bg_clr, bg_color=vary.bg_clr, border_color=vary.bg_clr, text_color=vary.font_clr)
        self.input_field.bind('<Enter>', lambda x: self.focus_text_entry(None, 0))
        self.input_field.bind('<Leave>', lambda x: self.focus_text_entry(None, 1))
        self.input_field.bind('<Return>', lambda x: self.add_text_bubble(None, 1, self.input_field.get()))
        self.input_field.bind('<Return>', self.check_inputs)

        # defining buttons
        self.menu_btn = ctk.CTkButton(
            self, text='', width=20, height=20, image=self.menu, fg_color=vary.bg_clr,
            hover_color=vary.widget_hover_clr)
        self.menu_btn.bind('<Button-1>', self.menu_btn_action)
        self.send_btn = ctk.CTkButton(
            self.bottom_panel, width=50, height=52, text='', fg_color=vary.bg_clr,
            hover_color=vary.widget_hover_clr, image=self.send)
        self.send_btn.bind('<Button-1>', lambda x: self.add_text_bubble(None, 1, self.input_field.get()))
        self.send_btn.bind('<Button-1>', self.check_inputs)

        # placing frames
        self.home_frame.pack()
        self.top_panel.grid(row=0, column=0, sticky='w')
        self.chat_panel.grid(row=1, column=0, sticky='w')
        self.bottom_panel.grid(row=2, column=0, sticky='w')

        # placing labels
        self.chat_dp.grid(row=0, column=0, padx=10, pady=5, rowspan=2)
        self.chat_name.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.date.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.cheat_lbl.grid(row=0, column=0)

        # placing text fields
        self.input_field.grid(row=0, column=0, sticky='w', padx=0)

        # placing buttons
        self.send_btn.grid(row=0, column=1, sticky='e', padx=0)
        self.menu_btn.place(x=vary.width-45, y=20)

        self.welcome_message()
    
    def welcome_message(self):
        hour = datetime.now().hour
        mzg = ''
        if (hour >= 6) and (hour < 12):
            mzg = f"Good Morning {vary.user_name}."
        elif (hour >= 12) and (hour < 16):
            mzg = f"Good afternoon {vary.user_name}."
        elif (hour >= 16) and (hour < 19):
            mzg = f"Good Evening {vary.user_name}."
        mzg = mzg + f"\nI am {vary.bot_name}. How may I assist you?"
        self.add_text_bubble(None, 2, mzg)

        self.menu_panel_widgets()

    def menu_panel_widgets(self):
        self.menu_panel = ctk.CTkFrame(self, fg_color=vary.bg_clr)

        self.settings_btn = ctk.CTkButton(
            self.menu_panel, text='Settings', fg_color=vary.widget_clr,
            hover_color=vary.widget_hover_clr)
        self.clear_chat_btn = ctk.CTkButton(
            self.menu_panel, text='Clear Chat', fg_color=vary.widget_clr,
            hover_color=vary.widget_hover_clr)
        self.exit_btn = ctk.CTkButton(
            self.menu_panel, text='Exit Chat', fg_color=vary.widget_clr,
            hover_color=vary.widget_hover_clr, command=lambda: exit())

        self.clear_chat_btn.bind('<Button-1>', self.clear_chat_btn_action)
        self.settings_btn.bind('<Button-1>', lambda x: self.settings_btn_action(None, 1))
        self.settings_panel_widgets()

    def settings_panel_widgets(self):
        self.settings_panel = ctk.CTkFrame(self, fg_color=vary.bg_clr)

        self.content_frame = ctk.CTkScrollableFrame(
            self.settings_panel, fg_color=vary.chat_bg_clr, width=vary.width+10, height=vary.height-10)

        self.img_4 = Image.open(f'Assets/Images/back.png')
        self.res_img_4 = self.img_4.resize((35, 35))
        self.back = ImageTk.PhotoImage(self.res_img_4)
        self.back_btn = ctk.CTkButton(
            self.settings_panel, text='', width=40, height=40, fg_color=vary.bg_clr, image=self.back,
            hover_color=vary.widget_clr, text_color=vary.font_clr, command=lambda: self.settings_btn_action(None, 0))
        self.lbl = ctk.CTkLabel(self.settings_panel, text='Settings', font=(vary.font_name, 40))

        self.user_inf_btn = ctk.CTkButton(
            self.content_frame, text='Bot Info', width=vary.width-10, height=40, fg_color=vary.bg_clr,
            hover_color=vary.widget_clr, text_color=vary.font_clr, font=(vary.font_name, 14), anchor='w',
            command=lambda: self.toggle_settings_btn(1))

        self.bot_inf_panel = ctk.CTkFrame(self.content_frame, fg_color=vary.chat_bg_clr)
        self.bot_name_lbl = ctk.CTkLabel(self.bot_inf_panel, text=f'Bot name:  {vary.bot_name}',
                                       anchor='w', justify='left')
        self.bot_new_name_lbl = ctk.CTkLabel(self.bot_inf_panel, text=f'Enter a \nnew name:', anchor='w',
                                             justify='left')
        self.bot_new_entry = ctk.CTkEntry(
            self.bot_inf_panel, font=(vary.font_name, vary.font_size), fg_color=vary.bg_clr
            , text_color=vary.font_clr, width=200)
        self.user_name_lbl = ctk.CTkLabel(self.bot_inf_panel, text=f'User name:  {vary.user_name}',
                                         anchor='w', justify='left')
        self.user_new_name_lbl = ctk.CTkLabel(self.bot_inf_panel, text=f'Enter a \nnew name:', anchor='w',
                                             justify='left')
        self.user_new_entry = ctk.CTkEntry(
            self.bot_inf_panel, font=(vary.font_name, vary.font_size), fg_color=vary.bg_clr
            , text_color=vary.font_clr, width=200)

        self.save_btn = ctk.CTkButton(self.bot_inf_panel, text='Save', fg_color=vary.bg_clr,
                                      hover_color=vary.widget_clr, text_color=vary.font_clr, width=150,
                                      command=self.save_btn_action)

        self.chat_panel_btn = ctk.CTkButton(
            self.content_frame, text='Chat settings', width=vary.width - 10, height=40, fg_color=vary.bg_clr,
            hover_color=vary.widget_clr, text_color=vary.font_clr, font=(vary.font_name, 14), anchor='w',
            command=lambda: self.toggle_settings_btn(2))

        self.chat_set_panel = ctk.CTkFrame(self.content_frame, fg_color=vary.chat_bg_clr)
        self.chat_icon_lbl = ctk.CTkLabel(self.chat_set_panel, text=f'Select chat icon:',
                                       anchor='w', justify='left')

        self.icon_1 = Image.open(f'Assets/Images/icon_0.png')
        self.res_icon_1 = self.icon_1.resize((60, 60))
        self.icon_1 = ImageTk.PhotoImage(self.res_icon_1)

        self.icon_2 = Image.open(f'Assets/Images/icon_1.png')
        self.res_icon_2 = self.icon_2.resize((60, 60))
        self.icon_2 = ImageTk.PhotoImage(self.res_icon_2)

        self.icon_3 = Image.open(f'Assets/Images/icon_2.png')
        self.res_icon_3 = self.icon_3.resize((60, 60))
        self.icon_3 = ImageTk.PhotoImage(self.res_icon_3)

        self.icon_4 = Image.open(f'Assets/Images/icon_3.png')
        self.res_icon_4 = self.icon_4.resize((60, 60))
        self.icon_4 = ImageTk.PhotoImage(self.res_icon_4)

        self.icon_1_btn = ctk.CTkButton(
            self.chat_set_panel, text='', width=60, height=60, fg_color=vary.bg_clr, image=self.icon_1,
            hover_color=vary.widget_clr, text_color=vary.font_clr, command=lambda: self.chat_icon_btn_action(0))
        self.icon_2_btn = ctk.CTkButton(
            self.chat_set_panel, text='', width=60, height=60, fg_color=vary.bg_clr, image=self.icon_2,
            hover_color=vary.widget_clr, text_color=vary.font_clr, command=lambda: self.chat_icon_btn_action(1))
        self.icon_3_btn = ctk.CTkButton(
            self.chat_set_panel, text='', width=60, height=60, fg_color=vary.bg_clr, image=self.icon_3,
            hover_color=vary.widget_clr, text_color=vary.font_clr, command=lambda: self.chat_icon_btn_action(2))
        self.icon_4_btn = ctk.CTkButton(
            self.chat_set_panel, text='', width=60, height=60, fg_color=vary.bg_clr, image=self.icon_4,
            hover_color=vary.widget_clr, text_color=vary.font_clr, command=lambda: self.chat_icon_btn_action(3))

        self.back_btn.place(x=5, y=5)
        self.lbl.pack()
        self.content_frame.pack()

        self.user_inf_btn.grid(row=0, column=0, padx=5, pady=5)
        self.chat_panel_btn.grid(row=2, column=0, padx=5, pady=5)
        self.chat_icon_lbl.grid(row=0, column=0, columnspan=4)
        self.icon_1_btn.grid(row=1, column=0)
        self.icon_2_btn.grid(row=1, column=1)
        self.icon_3_btn.grid(row=1, column=2)
        self.icon_4_btn.grid(row=1, column=3)
        self.bot_name_lbl.grid(row=0, column=0)
        self.bot_new_name_lbl.grid(row=1, column=0, padx=5, pady=5)
        self.bot_new_entry.grid(row=1, column=1, padx=5, pady=5)
        self.user_name_lbl.grid(row=2, column=0)
        self.user_new_name_lbl.grid(row=3, column=0, padx=5, pady=5)
        self.user_new_entry.grid(row=3, column=1, padx=5, pady=5)
        self.save_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def chat_icon_btn_action(self, what_is):
        txt = open('Assets\Data\icon.txt', 'w').write(str(what_is))
        vary.icon = what_is

        self.img_2 = Image.open(f'Assets/Images/icon_{vary.icon}.png')
        self.res_img_2 = self.img_2.resize((50, 50))
        self.dp = ImageTk.PhotoImage(self.res_img_2)

        self.chat_dp.configure(image=self.dp)

    def toggle_settings_btn(self, what_is):
        if what_is == 1:
            if vary.user_show:
                self.bot_inf_panel.grid_forget()
                vary.user_show = False
            else:
                self.bot_inf_panel.grid(row=1, column=0)
                vary.user_show = True

        if what_is == 2:
            if vary.chat_show:
                self.chat_set_panel.grid_forget()
                vary.chat_show = False
            else:
                self.chat_set_panel.grid(row=3, column=0)
                vary.chat_show = True

    def save_btn_action(self):
        if self.bot_new_entry.get() != '':
            vary.bot_name = self.bot_new_entry.get()

        if self.user_new_entry.get() != '':
            vary.user_name = self.user_new_entry.get()

        self.bot_new_entry.delete(0, ctk.END)
        self.user_new_entry.delete(0, ctk.END)

        txt = open('Assets\Data\\names.txt', 'w')
        txt.write(f'{vary.bot_name}\n{vary.user_name}')

        self.bot_name_lbl.configure(text=f'Bot name:  {vary.bot_name}')
        self.user_name_lbl.configure(text=f'User name:  {vary.user_name}')

        self.chat_name.configure(text=vary.bot_name)

    def settings_btn_action(self, args, what):
        if what == 1:
            self.menu_btn_action(None)

        if vary.settings_show:
            self.settings_panel.pack_forget()
            self.home_frame.pack()
            self.menu_btn.place(x=vary.width - 45, y=20)
            vary.settings_show = False
        else:
            self.settings_panel.pack()
            self.home_frame.pack_forget()
            self.menu_btn.place_forget()
            vary.settings_show = True

    def clear_chat_btn_action(self, args):
        self.chat_panel.destroy()
        self.chat_panel = ctk.CTkScrollableFrame(
            self.home_frame, fg_color=vary.chat_bg_clr, width=vary.width, height=vary.height - 130)
        self.cheat_lbl = ctk.CTkLabel(self.chat_panel, text='', height=1, width=vary.width - 10)
        self.chat_panel.grid(row=1, column=0)
        self.cheat_lbl.grid(row=0, column=0, padx=0, pady=0)
        self.menu_btn_action(None)
        self.welcome_message()

    def focus_text_entry(self, args, what_is):
        if what_is == 0:
            self.input_field.configure(fg_color=vary.widget_clr)
        else:
            self.input_field.configure(fg_color=vary.bg_clr)

    def menu_btn_action(self, args):
        if vary.menu_show:
            self.menu_panel.place_forget()
            self.settings_btn.grid_forget()
            self.clear_chat_btn.grid_forget()
            self.exit_btn.grid_forget()
            vary.menu_show = False
        else:
            self.menu_panel.place(x=vary.width-150, y=50)
            self.settings_btn.grid(row=0, column=0, padx=5, pady=2.5)
            self.clear_chat_btn.grid(row=1, column=0, padx=5, pady=2.5)
            self.exit_btn.grid(row=2, column=0, padx=5, pady=2.5)
            vary.menu_show = True

    def add_text_bubble(self, args, which_one, text):
        try:
            if not len(text) == 0:
                vary.inp = ''
                vary.inp = text
                self.input_field.delete(0, ctk.END)

                wrap = tw.TextWrapper(width=30)
                txt = wrap.wrap(text=text)
                text = ''

                for i in txt:
                    text = text + i + '\n'
                text = text[0:-1]

                self.txt = ctk.CTkLabel(self.chat_panel, text=text, corner_radius=10,
                                        font=(vary.font_name, vary.font_size))

                if which_one == 1:
                    self.txt.configure(anchor='e')
                    self.txt.configure(justify='right')
                    self.txt.configure(fg_color=vary.chat_send_clr)
                    self.txt.configure(text_color=vary.bg_clr)
                    self.txt.grid(row=vary.iterator, column=0, pady=2, sticky='e')

                if which_one == 2:
                    self.txt.configure(anchor='w')
                    self.txt.configure(justify='left')
                    self.txt.configure(fg_color=vary.chat_receive_clr)
                    self.txt.configure(text_color=vary.font_clr)
                    self.txt.grid(row=vary.iterator, column=0, pady=2, sticky='w', ipadx=6, ipady=6)

                vary.iterator += 1
        except Exception as e:
            print(e)

    def check_inputs(self, args):
        self.input_field.focus()
        if len(vary.inp) > 0:
            text = open('Assets\Data\\history.txt', 'r').read()
            gr.start(vary.inp.lower())
            val = f'{vary.inp}-{vary.reply}'
            if val not in text:
                text = f'{text}{val}\n'
                txt = open('Assets\Data\\history.txt', 'w')
                txt.write(text)
                txt.close()
            with open('Assets\Data\\history.txt', 'r') as f:
                vary.history = f.read().splitlines()
            self.add_text_bubble(None, 2, vary.reply)


