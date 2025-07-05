import { render, screen, fireEvent, waitFor, within } from '@testing-library/react'
import FileUploader from '../../src/components/FileUploader'
import uploadService from '../../src/services/uploadService'
import { toast } from 'sonner'

vi.mock('../../src/services/uploadService')
vi.mock('sonner', () => ({
  toast: {
    success: vi.fn(),
    error: vi.fn(),
  },
}))

describe('FileUploader', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders without crashing', () => {
    render(<FileUploader />)
    expect(screen.getByText(/Classificador de E-mails/i)).toBeInTheDocument()
  })

  it('uploads text and shows result', async () => {
    uploadService.uploadText.mockResolvedValue({
      categoria: "Produtivo",
      resposta_sugerida: "Obrigado pelo contato",
    })

    render(<FileUploader />)
    const textarea = screen.getByPlaceholderText(/Ou cole o conteúdo do email/i)
    await fireEvent.change(textarea, { target: { value: "Olá, gostaria de saber sobre faturas." } })
    const button = screen.getByRole('button')
    await fireEvent.click(button)

    await waitFor(() => {
      expect(screen.getByText(/Obrigado pelo contato/i)).toBeInTheDocument()
    })
    expect(toast.success).toHaveBeenCalledWith("Analisado com sucesso!")
  })

  it('click on history brings result back', async () => {
    uploadService.uploadText.mockResolvedValue({
      categoria: "Produtivo",
      resposta_sugerida: "Re-used response",
    })

    render(<FileUploader />)
    const textarea = screen.getByPlaceholderText(/Ou cole o conteúdo do email/i)
    await fireEvent.change(textarea, { target: { value: "Histórico test" } })
    const button = screen.getByRole('button')
    await fireEvent.click(button)

    await waitFor(() => {
      expect(screen.getByText(/Re-used response/i)).toBeInTheDocument()
    })

    const historySection = screen.getByText(/Histórico/i).closest('div')
    const historyItem = within(historySection).getByText(/Texto inserido/i)
    await fireEvent.click(historyItem)

    await waitFor(() => {
      expect(screen.getByText(/Re-used response/i)).toBeInTheDocument()
    })
  })
})
