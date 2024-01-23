from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Currículo - Webert Melo Moreira', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        body = body.replace('•', '*')
        self.multi_cell(0, 10, body.encode('latin-1', 'replace').decode('latin-1'))
        self.ln()

pdf = PDF()

pdf.add_page()

pdf.set_auto_page_break(auto=True, margin=15)

pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'WEBERT MELO MOREIRA', 0, 1, 'C')
pdf.cell(0, 10, 'Contagem | Minas Gerais  | Celular: (31) 9 8973-1769', 0, 1, 'C')
pdf.cell(0, 10, 'E-mail: webert.melo@hotmail.com |', 0, 1, 'C')
pdf.cell(0, 10, 'Linkedin - https://www.linkedin.com/in/webert-melo', 0, 1, 'C')
pdf.cell(0, 10, 'GITHUB - https://github.com/Xushuu', 0, 1, 'C')
pdf.ln(10)

pdf.chapter_title('Estágio em Desenvolvimento Back-End')
pdf.chapter_body('Estou à procura de uma oportunidade onde possa mostrar meus conhecimentos. Dedicado a desenvolver interfaces de usuário interativas e eficientes, estou motivado para me integrar a uma equipe dinâmica, contribuindo ativamente enquanto aprimoro minhas habilidades através de experiências práticas.')
pdf.ln(10)

pdf.chapter_title('EDUCAÇÃO')
pdf.chapter_body('Sistemas de Informação _ Faculdade Pitágoras, 2024 _ Em andamento\n'
                 'Analise e Desenvolvimento de Sistemas _ Faculdade Pitágoras, 2023 - Concluído\n'
                 'Principais disciplinas: Algoritmos E Programação Estruturada, Linguagem Orientada A Objetos, Interface E Usabilidade, Engenharia De Software, Ed - Mindset Ágil.')
pdf.ln(10)

pdf.chapter_title('CURSOS RELEVANTES')
pdf.chapter_body('Lógica de Programação Essencial | Introdução a Ciência de Dados | Lingua Inglesa I e II | Lógica de Programação Python | Assistente de Recursos Humanos')
pdf.ln(10)

pdf.chapter_title('ATIVIDADES DE LIDERANÇA E INTERESSE')
pdf.chapter_body('P.M. | SISPAG (novembro/2014 a março/2019) O que eu fiz: Gestão do sistema de pagamento de pensões do IPSEMG, acompanhamento de evoluções no sistema, aprimoramento de funcionalidades para o sistema, acompanhar o desenvolvimento do sistema, realizar testes para disponibilização das funcionalidades em ambiente de produção.')
pdf.ln(10)

pdf.chapter_title('HABILIDADES')
pdf.chapter_body('Gitlab | GitHub | VSCode | Trabalho em Equipe | Comunicação | Resolução de problemas | Facilidade de Aprendizado | Dinamismo | Python | Html | Css | JavaScript | Flexibilidade')
pdf.ln(10)

pdf.chapter_title('EXPERIÊNCIA PROFISSIONAL OU PROJETOS RELEVANTES')
pdf.chapter_body('Estagiário | PRODEMGE (Março 2023 até Dezembro 2023)\n'
                 '• Gestão de projetos;\n'
                 '• Experiência em planejamento e monitoramento;\n'
                 '• Comunicação com clientes e equipes, negociação;\n'
                 '• Levantamento de Requisitos de sistemas;\n'
                 '• Realização de teste funcionais e exploratórios;\n'
                 '• Criação de protótipos com AdobeXD.\n\n'
                 'Projetista | Costa Martins Engenharia (janeiro/2021 até Abril/2023)\n'
                 '• Gestão de Tempo;\n'
                 '• AUTOCAD;\n'
                 '• Gestão de Recursos;\n'
                 '• Acompanhamento de serviços;\n'
                 '• Tomada de Decisão\n\n'
                 'Chefe de Departamento | IPSEMG (janeiro/2018 até março/2019)\n'
                 '• Gestão de Equipe;\n'
                 '• Planejamento e acompanhamento de Metas;\n'
                 '• Elaboração de relatórios estatísticos;\n'
                 '• Tomada de Decisão\n'
                 '• Liderança;\n\n'
                 'Coordenador de setor - IPSEMG (novembro/2014 até dezembro/2017)\n'
                 '• Gestão de Equipe;\n'
                 '• Planejamento e acompanhamento de Metas;\n'
                 '• Elaboração de relatórios estatísticos;\n'
                 '• Tomada de Decisão;\n'
                 '• Liderança;\n\n'
                 'Assessor de setor | IPSEMG (outubro/2012 até setembro/2014)\n'
                 '• Gestão de Equipe;\n'
                 '• Elaboração de relatórios estatísticos;\n'
                 '• Controle de estagiários;\n'
                 '• Comunicação com clientes e equipes, negociação;\n\n'
                 'Auxiliar Administrativo - MGS (fevereiro/2008 a abril/2015)\n'
                 '• Rotinas Administrativas;\n'
                 '• Atendimento ao Público;\n'
                 '• Elaboração de relatórios estatísticos;')

pdf.output('curriculo_webert_melo.pdf')
